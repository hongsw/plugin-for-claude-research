#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PLUGIN_NAME = 'pdf-research';
const SKILL_NAME = 'pdf-research';

// Detect available CLIs
function detectCLIs() {
  const clis = [];

  try {
    execSync('which claude', { stdio: 'ignore' });
    clis.push('claude');
  } catch (e) {}

  try {
    execSync('which codex', { stdio: 'ignore' });
    clis.push('codex');
  } catch (e) {}

  return clis;
}

// Get CLI home directory
function getCliHome(cli) {
  const home = process.env.HOME || process.env.USERPROFILE;
  return path.join(home, `.${cli}`);
}

// Copy directory recursively
function copyDir(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);

      // Preserve executable permissions for .sh and .py files
      if (entry.name.endsWith('.sh') || entry.name.endsWith('.py')) {
        fs.chmodSync(destPath, '755');
      }
    }
  }
}

// Check Python dependencies
function checkPythonDeps() {
  try {
    execSync('python3 --version', { stdio: 'ignore' });
    return true;
  } catch (e) {
    return false;
  }
}

// Main installation
function install() {
  console.log(`\n📄 Installing ${PLUGIN_NAME} plugin...\n`);

  const clis = detectCLIs();

  if (clis.length === 0) {
    console.log('Warning: No supported CLI found (claude or codex)');
    console.log('   Please install Claude Code first: npm install -g @anthropic/claude-code');
    process.exit(1);
  }

  console.log(`Detected CLIs: ${clis.join(', ')}`);

  const sourceSkillDir = path.join(__dirname, '..', 'skills', SKILL_NAME);

  if (!fs.existsSync(sourceSkillDir)) {
    console.error(`Error: Source skill directory not found: ${sourceSkillDir}`);
    process.exit(1);
  }

  for (const cli of clis) {
    const cliHome = getCliHome(cli);
    const targetSkillDir = path.join(cliHome, 'skills', SKILL_NAME);

    console.log(`\nInstalling to ${cli}...`);

    // Create skills directory if it doesn't exist
    if (!fs.existsSync(path.join(cliHome, 'skills'))) {
      fs.mkdirSync(path.join(cliHome, 'skills'), { recursive: true });
    }

    // Copy skill files
    copyDir(sourceSkillDir, targetSkillDir);

    console.log(`   Installed skill to: ${targetSkillDir}`);
  }

  // Check Python availability
  const hasPython = checkPythonDeps();

  console.log(`
================================================================================
  ${PLUGIN_NAME} installed successfully!
================================================================================

  Components:
    - SKILL.md           - Skill documentation
    - .mcp.json          - MCP server configuration
    - prompts/           - Claude Code prompts
    - scripts/           - Python indexing and search scripts

  Scripts Location:
    ~/.claude/skills/${SKILL_NAME}/scripts/

  Setup:
    1. Install Python dependencies:
       cd ~/.claude/skills/${SKILL_NAME}/scripts
       pip install -r requirements.txt

    2. Set your OpenAI API key:
       export OPENAI_API_KEY=sk-your-key

  Usage:
    Index PDFs:
      python index_pdfs.py --pdf-dir /path/to/pdfs

    Search:
      python search.py "your query"

    Interactive:
      python search.py

${!hasPython ? '  Warning: Python 3 not found. Please install Python 3.10+\n' : ''}
================================================================================
`);
}

// Run installation
install();
