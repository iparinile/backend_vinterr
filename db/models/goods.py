from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, BOOLEAN, Float

from db.models import BaseModel


class DBGoods(BaseModel):
    __tablename__ = 'Goods'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    article = Column(VARCHAR(255), unique=True, nullable=False)
    good_1c_id = Column(VARCHAR(255), unique=True)
    category_id = Column(Integer, ForeignKey('Categories.id', ondelete='SET NULL'), nullable=False)
    barcode = Column(VARCHAR(255))
    structure_id = Column(Integer, ForeignKey('Structures.id', ondelete='SET NULL'), nullable=False)
    products_care_id = Column(Integer, ForeignKey('Products_care.id', ondelete='SET NULL'))
    description = Column(VARCHAR(), nullable=False)
    default_variation = Column(Integer, ForeignKey('Variations.id', ondelete='SET NULL'))
    is_visible = Column(BOOLEAN(), default=True)
    is_delete = Column(BOOLEAN(), default=False)
    weight = Column(Float)
