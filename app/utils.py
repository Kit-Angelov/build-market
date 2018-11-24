from .models import TagService, TagProduct


def tag_parser_service(service):
    name = service.name
    works = service.servicework_set.all()
    contractor = service.contractor

    tags = list()

    # parse name
    tags.append(str(name).lower())

    for name_elem in str(name).split():
        tags.append(str(name_elem).lower())

    # parse works
    for work in works:
        work_name = work.name
        tags.append(str(work_name).lower())
        for name_elem in str(work_name).split():
            tags.append(str(name_elem).lower())

    # parse contractor
    tags.append(str(contractor.name).lower())
    for name_elem in str(contractor.name).split():
        tags.append(str(name_elem).lower())

    for elem in tags:
        tag_service = TagService.objects.get_or_create(text=elem)
        tag_service.service.add(service)
        tag_service.save()


def tag_parser_product(product):
    name = product.name
    features = product.productfeature_set.all()
    store = product.store

    tags = list()

    # parse name
    tags.append(str(name).lower())

    for name_elem in str(name).split():
        tags.append(str(name_elem).lower())

    # parse features
    for feature in features:
        feature_title = feature.title
        feature_text = feature.text

        tags.append(str(feature_title).lower())
        tags.append(str(feature_text).lower())

        for title_elem in str(feature_title).split():
            tags.append(str(title_elem).lower())
        for text_elem in str(feature_text).split():
            tags.append(str(text_elem).lower())

    # parse store
    tags.append(str(store.name).lower())
    for name_elem in str(store.name).split():
        tags.append(str(name_elem).lower())

    for elem in tags:
        tag_product = TagProduct.objects.get_or_create(text=elem)
        tag_product.service.add(product)
        tag_product.save()
