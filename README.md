# Ditto Clipboard `.zdb` Extractor

This Python script converts `.zdb` clipboard history files created by the Ditto clipboard manager into clean, readable `.txt` files.

---

## ✅ Features

- Automatically decompresses `.zdb` (GZIP-compressed) files.
- Extracts only text-based clipboard entries.
- Saves a clean, readable `.txt` file.
- Works fully offline.

---

## 📦 Requirements

- Python 3.6 or newer  
(No extra libraries needed — uses only built-in modules)

---

## 🛠 How to Use

1. **Place your `.zdb` file** in the same folder as the script.
2. Rename it (optional) to: `Ditto Clipboard History.zdb`
3. Open terminal or command prompt:
   ```bash
   python ditto_zdb_to_txt.py
   ```
4. ✅ A file named `clipboard_output.txt` will be created in the same folder.

---

## 📁 Example

```bash
📂 Folder
├── Ditto Clipboard History.zdb
├── ditto_zdb_to_txt.py
└── clipboard_output.txt  ← result
```

---

## 🛡️ Notes

- Your data is never uploaded or stored — the script runs locally.
- You can modify the output format as needed (e.g. JSON, CSV).

---

## 📜 License

Free to use and modify. MIT License.