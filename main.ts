import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
// The wrapper is intentionally filesystem-only for the server-way harness.
mkdirSync(out, { recursive: true });
copyFileSync(join(dirname(new URL(import.meta.url).pathname), 'entry.png'), join(out, 'entry.png'));
