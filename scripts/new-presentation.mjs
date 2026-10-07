#!/usr/bin/env node

import { execSync } from 'node:child_process';
import process from 'node:process';

const args = process.argv.slice(2);
const rawName = args[0];

if (!rawName) {
  console.log(`
\x1b[31m[FEHLER]\x1b[0m Bitte gib einen Namen für die Präsentation an.

\x1b[36mBeispiel:\x1b[0m
  npm run new t2000-praxisarbeit
  npm run new bachelor-thesis
  npm run new presentation/ki-symposium
`);
  process.exit(1);
}

const branchName = rawName.startsWith('presentation/') ? rawName : `presentation/${rawName}`;

console.log(`\x1b[34m[DHBW Marp]\x1b[0m Erstelle neuen Präsentations-Branch: \x1b[32m${branchName}\x1b[0m ...`);

try {
  // Ensure we are branching off main
  execSync('git checkout main', { stdio: 'inherit' });
  execSync(`git checkout -b ${branchName}`, { stdio: 'inherit' });

  console.log(`
\x1b[32m✔ Branch '${branchName}' erfolgreich erstellt und ausgecheckt!\x1b[0m

\x1b[1mNächste Schritte:\x1b[0m
  1. Bearbeite \x1b[36mslides.md\x1b[0m mit deinen Inhalten.
  2. Starte den Live-Server mit \x1b[33mnpm start\x1b[0m (oder drücke \x1b[33mF5\x1b[0m in VS Code).
  3. Committe deine Folien in diesem Branch:
     \x1b[90mgit add slides.md assets/\x1b[0m
     \x1b[90mgit commit -m "feat: Folien für ${branchName} erstellt"\x1b[0m
`);
} catch (err) {
  console.error(`\x1b[31m[FEHLER]\x1b[0m Branch konnte nicht erstellt werden:`, err.message);
  process.exit(1);
}
