#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PLUGIN_NAME = 'domain-research';
const SKILL_NAMES = ['domain-research', 'self-learning'];

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

      // Preserve executable permissions for .sh files
      if (entry.name.endsWith('.sh')) {
        fs.chmodSync(destPath, '755');
      }
    }
  }
}

// Main installation
function install() {
  console.log(`\n🔬 Installing ${PLUGIN_NAME} plugin...\n`);

  const clis = detectCLIs();

  if (clis.length === 0) {
    console.log('⚠️  No supported CLI found (claude or codex)');
    console.log('   Please install Claude Code first: npm install -g @anthropic/claude-code');
    process.exit(1);
  }

  console.log(`📍 Detected CLIs: ${clis.join(', ')}`);

  for (const skillName of SKILL_NAMES) {
    const sourceSkillDir = path.join(__dirname, '..', 'skills', skillName);

    if (!fs.existsSync(sourceSkillDir)) {
      console.log(`⚠️  Skill directory not found: ${sourceSkillDir} (skipping)`);
      continue;
    }

    for (const cli of clis) {
      const cliHome = getCliHome(cli);
      const targetSkillDir = path.join(cliHome, 'skills', skillName);

      console.log(`\n📦 Installing ${skillName} to ${cli}...`);

      // Create skills directory if it doesn't exist
      if (!fs.existsSync(path.join(cliHome, 'skills'))) {
        fs.mkdirSync(path.join(cliHome, 'skills'), { recursive: true });
      }

      // Copy skill files
      copyDir(sourceSkillDir, targetSkillDir);

      console.log(`   ✅ Installed skill to: ${targetSkillDir}`);
    }
  }

  console.log(`
╔════════════════════════════════════════════════════════════╗
║  🎉 ${PLUGIN_NAME} installed successfully!                 ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  📚 Available Skills:                                      ║
║                                                            ║
║  1. domain-research (리서치 파이프라인)                      ║
║    • intent-analyzer.md   - Conversational discovery       ║
║    • key-questions.md     - Research question generation   ║
║    • research-gaps.md     - Gap identification             ║
║    • insight-extraction.md - Source analysis               ║
║    • multi-source-synthesis.md - Integration               ║
║    • practical-application.md - Action planning            ║
║    • comprehensive-guide.md - Final roadmap                ║
║                                                            ║
║  2. self-learning (자기주도 학습)                            ║
║    • Block 0-6: Claude Code 핵심 기능 학습                  ║
║    • STOP 프로토콜 기반 인터랙티브 학습                       ║
║    • 스킬 만들기 실습 포함                                   ║
║                                                            ║
║  🚀 Quick Start:                                           ║
║    /research  → "I want to research [topic]"               ║
║    /self-learning → Claude Code 학습 시작                   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
`);
}

// Run installation
install();
