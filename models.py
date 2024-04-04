from datetime import date
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, pk, crated_dt, updated_dt


class TradingResults(Base):
    __tablename__ = "spimex_trading_results"

    id: Mapped[pk]
    exchange_product_id: Mapped[str] = mapped_column(String(11))
    exchange_product_name: Mapped[str] = mapped_column(nullable=True)
    oil_id: Mapped[str] = mapped_column(String(4))
    delivery_basis_id: Mapped[str] = mapped_column(String(3))
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str] = mapped_column(String(1))
    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]
    date: Mapped[date]
    created_on: Mapped[crated_dt]
    updated_on: Mapped[updated_dt]
