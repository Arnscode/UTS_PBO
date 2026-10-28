from processors.base_processor import BaseProcessor
from processors.employee_processor import EmployeeProcessor
from processors.sensor_processor import SensorProcessor

def run_pipeline():
    tasks = [
        (EmployeeProcessor("data/employee.json"), "employees", "output/employee_report.csv"),
        (SensorProcessor("data/sensor_logs.json"), "readings", "output/sensor_report.csv")
    ]
    # Polymorphism: setiap objek menjalankan method yang sama dari kelas dasar.
    for processor, json_key, output_path in tasks:
        print(f"\\n>>> {processor.__class__.__name__}")
        processor.load_data(json_key)
        processor.process_data()
        processor.export_to_csv(output_path)
    print("\\n=== PIPELINE SELESAI ===")

if __name__ == "__main__":
    run_pipeline()
