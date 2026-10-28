from processors.base_processor import BaseProcessor

class SensorProcessor(BaseProcessor):
    """Processor sensor; field sumber dipertahankan sesuai soal UTS."""
    def process_data(self):
        # Override: transformasi seluruh pembacaan dari key "readings".
        if not self.raw_data:
            self.processed_data = []
            return []
        self.processed_data = list(map(
            lambda item: {
                "sensor_id": item["sensor_id"],
                "location": item["location"],
                "temperature": float(item["temperature"]),
                "status": item["status"],
                "operator_id": item["operator_id"],
                "action": "SEGERA DIPERIKSA" if item["status"] == "DANGER"
                          else ("PERLU PEMANTAUAN" if item["status"] == "WARNING" else "NORMAL")
            },
            self.raw_data
        ))
        print(f"[INFO] Memproses {len(self.processed_data)} pembacaan sensor.")
        return self.processed_data
