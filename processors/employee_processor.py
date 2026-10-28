from processors.base_processor import BaseProcessor

class EmployeeProcessor(BaseProcessor):
    """Processor karyawan; field sumber dipertahankan sesuai soal UTS."""
    def process_data(self):
        # Override: transformasi seluruh karyawan dari key "employees".
        if not self.raw_data:
            self.processed_data = []
            return []
        self.processed_data = list(map(
            lambda emp: {
                "emp_id": emp["emp_id"],
                "name": emp["name"],
                "is_permanent": emp["is_permanent"],
                "employment_status": "TETAP" if emp["is_permanent"] else "KONTRAK",
                "base_salary": float(emp["base_salary"]),
                "bonus_code": emp["bonus_code"]
            },
            self.raw_data
        ))
        print(f"[INFO] Memproses {len(self.processed_data)} data karyawan.")
        return self.processed_data
