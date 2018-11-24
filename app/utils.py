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
