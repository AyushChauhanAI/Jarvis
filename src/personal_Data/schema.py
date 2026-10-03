from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class Profile(BaseModel):

    # ── Name ─────────────────────────────────────
    first: Optional[str] = Field(None)

    # ── Birth ─────────────────────────────────────
    date_of_birth: Optional[date] = Field(None)
    time_of_birth: Optional[str] = Field(None)

    place_of_birth_city: Optional[str] = Field(None)
    place_of_birth_state: Optional[str] = Field(None)
    place_of_birth_country: Optional[str] = Field(None)

    birth_hospital_name: Optional[str] = Field(None)
    birth_type: Optional[str] = Field(None)
    was_premature_birth: Optional[bool] = Field(None)

    # ── Gender & Blood ───────────────────────────
    gender: Optional[str] = Field(None)
    blood_group: Optional[str] = Field(None)

    # ── Religion & Culture ───────────────────────
    religion: Optional[str] = Field(None)
    caste: Optional[str] = Field(None)
    sub_caste: Optional[str] = Field(None)
    gotra: Optional[str] = Field(None)
    community: Optional[str] = Field(None)

    # ── Work ─────────────────────────────────────
    work_mode: Optional[str] = Field(None)
    company_type: Optional[str] = Field(None)

    # ── Education ────────────────────────────────
    education_board: Optional[str] = Field(None)
    degree_type: Optional[str] = Field(None)