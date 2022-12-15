import datetime
from jinja2 import Template, Environment, FileSystemLoader


class TemplateManager:
    _environment: Environment

    def resolve_template(self, template, data: dict):
        template_renderer = Template(template)
        return template_renderer.render(data=data)

    def init_env(self, template_path: str):
        file_loader = FileSystemLoader(template_path)
        self._environment = Environment(loader=file_loader)

    def set_extension(self, extensions):
        for extension in extensions:
            self._environment.add_extension(extension)

    def add_global_variables(self, template):
        template.globals['show_year'] = datetime.datetime.today().year
        return template

    def get_template(self, template_name) -> Template:
        template = self._environment.get_template(template_name)
        template = self.add_global_variables(template)
        return template

    def resolve(self, template_name, data):
        template = self.get_template(template_name)
        return template.render(data=data)
