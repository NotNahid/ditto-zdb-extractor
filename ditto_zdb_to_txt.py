import gzip
import sqlite3
from io import BytesIO

def extract_clipboard_from_zdb(zdb_path, output_txt_path):
    """
    Converts a Ditto clipboard .zdb file into a readable .txt file.
    """

    # Step 1: Read and decompress GZIP file
    with open(zdb_path, 'rb') as f:
        raw_data = f.read()

    with gzip.GzipFile(fileobj=BytesIO(raw_data)) as gz:
        decompressed_data = gz.read()

    # Step 2: Save the decompressed SQLite DB to a temp file
    temp_db_path = "temp_ditto.db"
    with open(temp_db_path, "wb") as f:
        f.write(decompressed_data)

    # Step 3: Connect to the SQLite database
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()

    # Step 4: Query for clipboard entries that are text-based
    cursor.execute("""
        SELECT ooData FROM Data
        WHERE strClipBoardFormat LIKE '%text%' OR strClipBoardFormat LIKE '%CF_TEXT%'
    """)
    rows = cursor.fetchall()

    # Step 5: Decode BLOBs into text strings
    output = []
    for row in rows:
        try:
            text = row[0].decode("utf-8", errors="ignore").strip()
            if text:
                output.append(text)
        except:
            continue

    conn.close()

    # Step 6: Save all cleaned text into a .txt file
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(output))

    print(f"✅ Conversion complete. Saved to: {output_txt_path}")

# 👉 Update the filename if needed
extract_clipboard_from_zdb("Ditto Clipboard History.zdb", "clipboard_output.txt")