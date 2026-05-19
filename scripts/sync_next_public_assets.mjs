import { cp, mkdir, rm } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const CARD_FOLDERS = [
  "actions",
  "debriefs",
  "events",
  "posts",
  "roles",
  "strategies",
  "tasks",
];

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourceRoot = path.join(root, "card", "final", "v2");
const targetRoot = path.join(root, "public", "card", "final", "v2");

await rm(targetRoot, { recursive: true, force: true });

let copiedFolders = 0;
for (const folder of CARD_FOLDERS) {
  const source = path.join(sourceRoot, folder);
  const target = path.join(targetRoot, folder);
  await mkdir(path.dirname(target), { recursive: true });
  await cp(source, target, {
    recursive: true,
    filter: (entry) => entry.endsWith(".png") || !path.extname(entry),
  });
  copiedFolders += 1;
}

console.log(`Synced ${copiedFolders} card asset folders to public/card/final/v2.`);
