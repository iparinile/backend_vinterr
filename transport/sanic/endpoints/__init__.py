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

from .sizes.size import SizeEndpoint
from .sizes.create import CreateSizeEndpoint
from .sizes.get_all import GetAllSizesEndpoint

from .colors.color import ColorEndpoint
from .colors.create import CreateColorEndpoint
from .colors.get_all import GetAllColorsEndpoint

from .goods.create import CreateGoodEndpoint
from .goods.get_all import GetAllGoodsEndpoint
from .goods.get_variations import GetVariationsForGoodEndpoint
from .goods.good import GoodEndpoint

from .variations.create import CreateVariationEndpoint
from .variations.get_all import GetAllVariationsEndpoint
from .variations.get_variation import GetVariationEndpoint
from .variations.variation import VariationEndpoint

from .images.image import ImageEndpoint
from .images.create import CreateImageEndpoint

from .orders.create import CreateOrderEndpoint
from .orders.get_all import GetAllOrdersEndpoint
from .orders.order import OrderEndpoint

from .contact_forms.create import CreateContactFormEndpoint

from .delivery_types.create import CreateDeliveryTypeEndpoint
from .delivery_types.get_all import GetAllDeliveryTypesEndpoint
