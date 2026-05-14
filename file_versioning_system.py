import os
import shutil
import json
from datetime import datetime
from pathlib import Path

# Configuration
VERSIONS_DIR = 'versions'
METADATA_FILE = 'versions_metadata.json'

def ensure_version_dir():
    # Create versions directory if it doesn't exist
    os.makedirs(VERSIONS_DIR, exist_ok=True)

def load_metadata():
    # Load version metadata from JSON file
    if not os.path.exists(METADATA_FILE):
        return []
    try:
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    except (json.decoder.JSONDecodeError, IOError):
        return []

def save_metadata(metadata):
    # Save version metadata to JSON file
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

def get_versioned_filename(original_name,
                           timestamp):
    # Create a versioned filename with datestamp
    name, ext = os.path.splitext(original_name)
    return f'{name}_{timestamp}.{ext}'

def create_version(file_path):
    #Create a new version of the given file
    if not os.path.exists(file_path):
        print(f'File not found: {file_path}')
        return False
    ensure_version_dir()
    metadata = load_metadata()

    filename = os.path.basename(file_path)
    print(f'Filename: {filename}')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    print(f'Timestamp: {timestamp}')
    version_name = get_versioned_filename(filename, timestamp)
    print(f'Version name: {version_name}')
    version_path = os.path.join(VERSIONS_DIR, version_name)
    print(f'Version path: {version_path}')

    try:
        # Copy the current file to versions folder
        shutil.copy2(file_path, version_path)

        # Update metadata
        if filename not in metadata:
            metadata[filename] = []

        metadata[filename].append({
            'version_name': version_name,
            'timestamp': timestamp,
            'size': os.path.getsize(version_path),
            'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        save_metadata(metadata)
        print('Version created: {version_name}')
        return True
    except Exception as e:
        print(f'Error creating version: {e}')
        return False

def list_versions(filename):
    # List all versions of a specific file
    metadata = load_metadata()
    if filename not in metadata or not metadata[filename]:
        print(f'No versions found for: {filename}')
        return

    print(f'\nVersions for {filename}:')
    print('-' * 70)
    for v in sorted(metadata[filename], key=lambda x: x['timestamp'], reverse=True):
        print(f'{v["version_name"]}')
        print(f'Date: {v["date_created"]}')
        print(f'Size: {v["size"] / 1024:.1f} KB')
        print('-' * 50)

def restore_version(filename, version_index=0):
    # Restore a previous version of the file (0=most recent)
    metadata = load_metadata()
    if filename not in metadata or not metadata[filename]:
        print(f'No versions available for: {filename}')
        return False

    versions = sorted(metadata[filename], key=lambda x: x['timestamp'], reverse=True)
    if version_index >= len(versions):
        print('Invalid version index')
        return False

    selected = versions[version_index]
    version_path = os.path.join(VERSIONS_DIR, selected['version_name'])

    if not os.path.exists(version_path):
        print('Version file missing')
        return False

    try:
        # Backup current version before overwriting
        current_backup = f'{filename}_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        shutil.copy2(version_path, current_backup)
        print(f'Current file backed up as: {current_backup}')

        # Restore the selected version
        shutil.copy2(version_path, filename)
        print(f'Restored version: {selected['version_name']}')
        return True
    except Exception as e:
        print(f'Restore failed: {e}')
        return False

def list_all_files():
    metadata = load_metadata()
    if not metadata:
        print('No versioned files yet')
        return

    print(f'\nFiles available for versioning:')
    for filename in metadata.keys():
        count = len(metadata[filename])
        latest = sorted(metadata[filename],
                        key=lambda x: x['timestamp'],
                        reverse=True)[0]['date_created']
        print(f'{filename} {count} versions, {latest} date')

def main():
    ensure_version_dir()
    print('Simple File Versioning System\n')

    while True:
        print('\n' + '=' * 50)
        print('1. Create new version of a file')
        print('2. List versions of a file')
        print('3. Restore a previous version')
        print('4. List all versioned files')
        print('5. Exit')
        print('=' * 50)

        choice = input('Choose an option (1-5): ').strip()

        if choice == '1':
            file_path = input('Enter file path to version (i.e., report.txt): ').strip()
            create_version(file_path)
        elif choice == '2':
            filename = input('Enter filename to list versions: ').strip()
            list_versions(filename)
        elif choice == '3':
            filename = input('Enter filename to restore (i.e., report.txt): ').strip()
            list_versions(filename)
            try:
                idx = int(input('\nEnter version index to restore (0 = latest): ') or 0)
                restore_version(filename, idx)
            except ValueError:
                print('Invalid index')
        elif choice == '4':
            list_all_files()
        elif choice == '5':
            print('Goodbye! Your versions are safely stored in the versions folder.')
            break
        else:
            print('Invalid choice. Please select 1-5.')

if __name__ == '__main__':
    main()