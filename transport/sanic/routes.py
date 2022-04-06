from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=['GET', 'POST']),
        endpoints.CreateUserEndpoint(config=config, context=context, uri='/users', methods=['POST', 'OPTIONS'],
                                     auth_required=True, is_administrator_access=True),
        endpoints.AuthUserEndpoint(config=config, context=context, uri='/users/auth', methods=['POST', 'OPTIONS']),
        endpoints.UserEndpoint(config=config, context=context, uri='/users/<user_id:int>', methods=['GET'],
                               auth_required=True, is_administrator_access=True),
        endpoints.CreateCustomerEndpoint(config=config, context=context, uri='/customers', methods=['POST', 'OPTIONS']),
        endpoints.AuthCustomerEndpoint(config=config, context=context, uri='/customers/auth',
                                       methods=['POST', 'OPTIONS']),
        endpoints.GetAllMaterialsEndpoint(config=config, context=context, uri='/materials/all', methods=['GET']),
        endpoints.CreateMaterialEndpoint(config=config, context=context, uri='/materials', methods=['POST', 'OPTIONS'],
                                         auth_required=True, is_administrator_access=True),
        endpoints.MaterialEndpoint(config=config, context=context, uri='/materials/<material_id:int>',
                                   methods=['GET', 'PATCH', 'DELETE'],
                                   auth_required=True, is_administrator_access=True),
        endpoints.GetAllCategoriesEndpoint(config=config, context=context, uri='/categories/all', methods=['GET']),
        endpoints.CreateCategoryEndpoint(config=config, context=context, uri='/categories', methods=['POST', 'OPTIONS'],
                                         auth_required=True, is_administrator_access=True),
        endpoints.CategoryEndpoint(config=config, context=context, uri='/categories/<category_id:int>',
                                   methods=['GET', 'PATCH', 'DELETE'],
                                   auth_required=True, is_administrator_access=True),
        endpoints.GetAllStructuresEndpoint(config=config, context=context, uri='/structures/all', methods=['GET']),
        endpoints.CreateStructureEndpoint(config=config, context=context, uri='/structures',
                                          methods=['POST', 'OPTIONS'], auth_required=True,
                                          is_administrator_access=True),
        endpoints.StructureEndpoint(config=config, context=context, uri='/structures/<structure_id:int>',
                                    methods=['GET', 'PATCH', 'DELETE'],
                                    auth_required=True, is_administrator_access=True),
        endpoints.GetAllSizesEndpoint(config=config, context=context, uri='/sizes/all', methods=['GET']),
        endpoints.CreateSizeEndpoint(config=config, context=context, uri='/sizes', methods=['POST', 'OPTIONS'],
                                     auth_required=True, is_administrator_access=True),
        endpoints.SizeEndpoint(config=config, context=context, uri='/sizes/<size_id:int>',
                               methods=['GET', 'PATCH', 'DELETE'],
                               auth_required=True, is_administrator_access=True),
        endpoints.GetAllColorsEndpoint(config=config, context=context, uri='/colors/all', methods=['GET']),
        endpoints.CreateColorEndpoint(config=config, context=context, uri='/colors', methods=['POST', 'OPTIONS'],
                                      auth_required=True, is_administrator_access=True),
        endpoints.ColorEndpoint(config=config, context=context, uri='/colors/<color_id:int>',
                                methods=['GET', 'PATCH', 'DELETE'],
                                auth_required=True, is_administrator_access=True),
        endpoints.CreateGoodEndpoint(config=config, context=context, uri='/goods', methods=['POST', 'OPTIONS'],
                                     auth_required=True, is_administrator_access=True),
        endpoints.GetAllGoodsEndpoint(config=config, context=context, uri='/goods/all', methods=['GET']),
        endpoints.GoodEndpoint(config=config, context=context, uri='/goods/<good_id:int>', methods=['GET']),
        endpoints.GetVariationsForGoodEndpoint(config=config, context=context, uri='/goods/<good_id:int>/variations',
                                               methods=['GET']),
        endpoints.CreateVariationEndpoint(config=config, context=context, uri='/variations',
                                          methods=['POST', 'OPTIONS'], auth_required=True,
                                          is_administrator_access=True),
        endpoints.GetAllVariationsEndpoint(config=config, context=context, uri='/variations/all', methods=['GET']),
        endpoints.GetVariationEndpoint(config=config, context=context, uri='/variations/<variation_id:int>',
                                       methods=['GET']),
        endpoints.VariationEndpoint(config=config, context=context, uri='/variations/<variation_id:int>',
                                    methods=['PATCH'], auth_required=True, is_administrator_access=True),
        endpoints.VariationEndpoint(config=config, context=context, uri='/variations/<variation_id:int>',
                                    methods=['OPTIONS']),
        endpoints.ImageEndpoint(config=config, context=context, uri='/images/<img_path:path>', methods=['GET']),
        endpoints.CreateImageEndpoint(config=config, context=context, uri='/images', methods=['POST'],
                                      auth_required=True, is_administrator_access=True),
        endpoints.CreateOrderEndpoint(config=config, context=context, uri='/orders', methods=['POST', 'OPTIONS']),
        endpoints.GetAllOrdersEndpoint(config=config, context=context, uri='/orders/all', methods=['GET'],
                                       auth_required=True, is_administrator_access=True),
        endpoints.OrderEndpoint(config=config, context=context, uri='/orders/<order_id:int>', methods=['GET', 'POST'],
                                auth_required=True, is_administrator_access=True),
        endpoints.RegisterPaymentsEndpoint(config=config, context=context, uri='/register_payment',
                                           methods=['POST', 'OPTIONS']),
        endpoints.GetStatusPaymentsEndpoint(config=config, context=context,
                                            uri='/orders/<sberbank_order_id:uuid>/status_payment',
                                            methods=['GET']),
        endpoints.CreateContactFormEndpoint(config=config, context=context, uri='/contact_forms',
                                            methods=['POST', 'OPTIONS']),
        endpoints.CreateDeliveryTypeEndpoint(config=config, context=context, uri='/delivery_types',
                                             methods=['POST', 'OPTIONS'], auth_required=True,
                                             is_administrator_access=True),
        endpoints.GetAllDeliveryTypesEndpoint(config=config, context=context, uri='/delivery_types/all',
                                              methods=['GET']),
        endpoints.CreateTelegramUserEndpoint(config=config, context=context, uri='/telegram_users', methods=['POST'],
                                             telegram_password_required=True),
        endpoints.TelegramUserEndpoint(config=config, context=context, uri='/telegram_users/<telegram_user_id:int>',
                                       methods=['GET', 'PATCH'], telegram_password_required=True)
    )
