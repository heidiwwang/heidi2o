import os
import re
import shutil
from pathlib import Path

# --- CONFIGURATION ---
OBSIDIAN_VAULT = Path('/home/hide/Documents/heidi2o/03_lab/')
OBSIDIAN_ATTACHMENTS = Path('/home/hide/Documents/heidi2o/02_library/attachments')
QUARTZ_CONTENT = Path('/home/hide/quartz/content')
QUARTZ_ATTACHMENTS = QUARTZ_CONTENT / "assets"

NOTE_FILENAME = "GovActionCafe_Pre-brief.md"

def process_content(content):
    # 1. Find the first H1 (e.g., # My Title)
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    
    if h1_match:
        h1_text = h1_match.group(1).strip()
        # 2. Remove the first H1 line from the content
        # This replaces the first occurrence of the H1 line with an empty string
        content = re.sub(r'^#\s+.+$\n?', '', content, count=1, flags=re.MULTILINE)
        
        # 3. Update the YAML title
        # Looks for title: followed by anything and replaces it
        if re.search(r'^title:.*$', content, re.MULTILINE):
            content = re.sub(r'^title:.*$', f'title: "{h1_text}"', content, flags=re.MULTILINE)
        else:
            # If no title field exists, insert it into the first YAML block found
            content = re.sub(r'^---', f'---\ntitle: "{h1_text}"', content, count=1)
            
    return content

def copy_to_quartz(note_name):
    note_matches = list(OBSIDIAN_VAULT.rglob(note_name))
    if not note_matches:
        print(f"❌ Error: {note_name} not found.")
        return
    
    source_path = note_matches[0]
    QUARTZ_CONTENT.mkdir(parents=True, exist_ok=True)
    QUARTZ_ATTACHMENTS.mkdir(parents=True, exist_ok=True)

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the H1 to YAML transformation
    updated_content = process_content(content)

    # Find attachments
    attachments = re.findall(r'!\[\[(.*?)\]\]', content)

    # Write the modified content to Quartz
    with open(QUARTZ_CONTENT / note_name, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"✅ Note processed and copied: {note_name}")

    # Copy attachments
    for asset_raw in attachments:
        asset_name = asset_raw.split('|')[0].strip()
        src_asset = OBSIDIAN_ATTACHMENTS / asset_name
        
        if not src_asset.exists():
            fallback = list(OBSIDIAN_ATTACHMENTS.rglob(asset_name))
            src_asset = fallback[0] if fallback else None

        if src_asset and src_asset.exists():
            shutil.copy2(src_asset, QUARTZ_ATTACHMENTS / asset_name)
            print(f"   📎 Attachment copied: {asset_name}")

if __name__ == "__main__":
    copy_to_quartz(NOTE_FILENAME)