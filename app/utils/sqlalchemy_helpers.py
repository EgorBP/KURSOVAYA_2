from sqlalchemy import MappingResult
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm import Query


def is_valid_column_for_model(column: InstrumentedAttribute, model: type) -> bool:
    """
    Проверяет, что переданный ключ является колонкой (атрибутом модели),
    и принадлежит указанной модели.

    :param column: проверяемый объект (ожидается ORM-атрибут).
    :param model: класс ORM-модели (например User).
    """

    return isinstance(column, InstrumentedAttribute) and column.class_ == model


def get_all_columns(model: type):
    """
    Возвращает список всех колонок SQLAlchemy-модели.

    :param model: SQLAlchemy-модель.
    :return: список колонок модели в формате [Model.col1, Model.col2, ...].
    """
    return [getattr(model, column.key) for column in model.__mapper__.columns]


def prepare_to_send(query: Query | MappingResult, class_: type):
    """
    Выполняет ORM-запрос и валидирует результаты через Pydantic-модель.
    """
    return [class_.model_validate(row) for row in query.all()]