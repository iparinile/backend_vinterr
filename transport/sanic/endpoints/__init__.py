from .base import BaseEndpoint
from .helth import HealthEndpoint

from .users.create import CreateUserEndpoint
from .users.auth import AuthUserEndpoint
from .users.user import UserEndpoint

from .customers.create import CreateCustomerEndpoint
from .customers.auth import AuthCustomerEndpoint

from .materials.create import CreateMaterialEndpoint
from .materials.material import MaterialEndpoint
from .materials.get_all import GetAllMaterialsEndpoint

from .categories.category import CategoryEndpoint
from .categories.create import CreateCategoryEndpoint
from .categories.get_all import GetAllCategoriesEndpoint


from .structures.structure import StructureEndpoint
from .structures.create import CreateStructureEndpoint
from .structures.get_all import GetAllStructuresEndpoint
