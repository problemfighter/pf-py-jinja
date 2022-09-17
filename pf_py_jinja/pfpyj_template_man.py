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

    def add_global_variables(self, template):
        template.globals['show_year'] = datetime.datetime.today().year
        return template

    def resolve(self, template_name, data):
        template = self._environment.get_template(template_name)
        template = self.add_global_variables(template)
        return template.render(data=data)
