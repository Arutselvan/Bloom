from qa.models import Question
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.forms.models import model_to_dict
from text_analysis.knowledge_extraction import KnowledgeExtractor

def get_weak_topics(user):
    question_ids = Question.objects.filter(user=user).values('id')
    question_content_type = ContentType.objects.get_for_model(Question) 
    tag_ids = TaggedItem.objects.filter(content_type=question_content_type, object_id__in=question_ids).values('tag_id')
    tags = Tag.objects.filter(pk__in=tag_ids)
    return [model_to_dict(tag) for tag in tags]

def perform_extraction(file_name):
	knowledge_extractor = KnowledgeExtractor()
	text = knowledge_extractor.ocr(file_name)
	summary = knowledge_extractor.get_summary(text)
	concepts = knowledge_extractor.get_concepts(text=text)
	clusters = knowledge_extractor.get_clusters(text)

	return {'text': text, 'summary': summary, 'concepts': concepts, 'clusters': clusters}
