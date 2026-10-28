import json, csv, os
from typing import List, Dict, Any

class BaseProcessor:
    """Kelas induk untuk membaca JSON dan mengekspor hasil ke CSV."""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.__raw_data: List[Dict[str, Any]] = []
        self.__processed_data: List[Dict[str, Any]] = []

    @property
    def raw_data(self): return self.__raw_data
    @raw_data.setter
    def raw_data(self, value): self.__raw_data = value

    @property
    def processed_data(self): return self.__processed_data
    @processed_data.setter
    def processed_data(self, value): self.__processed_data = value

    def load_data(self, json_key: str) -> None:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                payload = json.load(file)
            value = payload.get(json_key, [])
            self.raw_data = value if isinstance(value, list) else []
            print(f"[INFO] {self.__class__.__name__}: {len(self.raw_data)} data dimuat.")
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"[ERROR] Gagal membaca {self.file_path}: {error}")
            self.raw_data = []

    def process_data(self):
        raise NotImplementedError("Kelas turunan harus meng-override process_data().")

    def export_to_csv(self, output_path: str) -> None:
        if not self.processed_data:
            print("[WARNING] Tidak ada data untuk diekspor.")
            return
        folder = os.path.dirname(output_path)
        if folder: os.makedirs(folder, exist_ok=True)
        with open(output_path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=list(self.processed_data[0].keys()))
            writer.writeheader()
            writer.writerows(self.processed_data)
        print(f"[SUCCESS] Hasil disimpan: {output_path}")
