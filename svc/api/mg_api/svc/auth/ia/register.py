from attrs import define


# @define
# class RegisterIA:
#     _user: r.User
#     _agency: r.Agency
#
#     _db_sess: AsyncSession
#
#     async def __call__(self, dto: d.Register) -> None:
#         agency = await self._agency.create(**dto.agency.model_dump())
#         user = await self._user.create(**dto.user.model_dump())
#         user.agency = agency
#         user.role = m.RoleEnum.director
#         await self._db_sess.commit()
