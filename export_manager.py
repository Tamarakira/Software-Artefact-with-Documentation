
import pandas as pd
import os

class ExportHandler:
    def __init__(self, data):
        self.data = data

    def _generate_unique_filename(self, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = f"{base}_{counter}{ext}"
        while os.path.exists(new_filename):
            counter += 1
            new_filename = f"{base}_{counter}{ext}"
        return new_filename

    def export_to_csv(self, filename):
        if os.path.exists(filename):
            filename = self._generate_unique_filename(filename)
        self.data.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
