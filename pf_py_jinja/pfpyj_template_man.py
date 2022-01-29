from jinja2 import Template, Environment, FileSystemLoader


class TemplateManager:
    _environment: Environment

    def resolve_template(self, template, data: dict):
        template_renderer = Template(template)
        return template_renderer.render(data=data)

    def init_env(self, template_path: str):
        file_loader = FileSystemLoader(template_path)
        self._environment = Environment(loader=file_loader)

    def resolve(self, template_name, data):
        template = self._environment.get_template(template_name)
        return template.render(data=data)
