import os
import sys
import django

# Устанавливаем настройки Django для скрипта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "events.settings")

django.setup()

from django.apps import apps
from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField

def generate_dot():
    models = apps.get_models()
    with open('model_diagram.dot', 'w') as f:
        f.write('digraph models {\n')
        for model in models:
            # Для каждой модели получаем все связи
            for field in model._meta.fields + model._meta.many_to_many:
                if isinstance(field, (ForeignKey, OneToOneField, ManyToManyField)):
                    target = field.related_model
                    label = f"{field.name} ({field.get_internal_type()})"
                    f.write(f'  "{model.__name__}" -> "{target.__name__}" [label="{label}"];\n')
        f.write('}\n')

if __name__ == "__main__":
    generate_dot()
