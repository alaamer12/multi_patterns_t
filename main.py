from abc import ABC, abstractmethod

# Abstract class defining the template
class ReportTemplate(ABC):
    def create_report(self):
        report = self.open_template()
        report += self.fill_header()
        report += self.fill_body()
        report += self.fill_footer()
        report += self.close_template()
        return report

    @abstractmethod
    def open_template(self):
        pass

    @abstractmethod
    def fill_header(self):
        pass

    @abstractmethod
    def fill_body(self):
        pass

    @abstractmethod
    def fill_footer(self):
        pass

    @abstractmethod
    def close_template(self):
        pass

# Concrete implementation for a manager
class ManagerReport(ReportTemplate):
    def open_template(self):
        return "Manager's Report\n"

    def fill_header(self):
        return "Header: Manager\n"

    def fill_body(self):
        return "Body: Manager\n"

    def fill_footer(self):
        return "Footer: Manager\n"

    def close_template(self):
        return "End of Manager's Report"

# Concrete implementation for a developer
class DeveloperReport(ReportTemplate):
    def open_template(self):
        return "Developer's Report\n"

    def fill_header(self):
        return "Header: Developer\n"

    def fill_body(self):
        return "Body: Developer\n"

    def fill_footer(self):
        return "Footer: Developer\n"

    def close_template(self):
        return "End of Developer's Report"

# Client code
def main():
    manager_report = ManagerReport()
    developer_report = DeveloperReport()

    print(manager_report.create_report())
    print("\n")
    print(developer_report.create_report())

if __name__ == "__main__":
    main()
