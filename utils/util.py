from qa.models import Question
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.forms.models import model_to_dict

def get_weak_topics(user):
    question_ids = Question.objects.filter(user=user).values('id')
    question_content_type = ContentType.objects.get_for_model(Question) 
    tag_ids = TaggedItem.objects.filter(content_type=question_content_type, object_id__in=question_ids).values('tag_id')
    tags = Tag.objects.filter(pk__in=tag_ids)
    return [model_to_dict(tag) for tag in tags]

