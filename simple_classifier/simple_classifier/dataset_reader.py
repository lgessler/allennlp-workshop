import json
from typing import Dict, Iterable

from allennlp.data import DatasetReader, Instance, Field
from allennlp.data.fields import LabelField, TextField
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer


@DatasetReader.register("yelp-review-jsonl")
class YelpReviewJsonLinesReader(DatasetReader):
    def __init__(
        self,
        tokenizer: Tokenizer = None,
        token_indexers: Dict[str, TokenIndexer] = None,
        max_tokens: int = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.tokenizer = tokenizer or WhitespaceTokenizer()
        self.token_indexers = token_indexers or {"tokens": SingleIdTokenIndexer()}
        self.max_tokens = max_tokens

    def text_to_instance(self, text: str, label: str = None) -> Instance:  # type: ignore
        tokens = self.tokenizer.tokenize(text)
        if self.max_tokens:
            tokens = tokens[: self.max_tokens]
        text_field = TextField(tokens, self.token_indexers)
        fields: Dict[str, Field] = {"text": text_field}
        if label:
            fields["label"] = LabelField(label)
        return Instance(fields)

    def _read(self, file_path: str) -> Iterable[Instance]:
        with open(file_path, "r") as lines:
            for line in lines:
                if line != "":
                    data = json.loads(line)
                    # The text of the yelp review.
                    # Note we need to replace the escaped newline characters and double quotes.
                    text = data["text"]
                    text = text.replace("\\n", "\n")
                    text = text.replace('\\"', '"')
                    # The rating--these are numbers 0 through 4, make them strings "1" to "5"
                    label = str(1 + data["label"])
                    yield self.text_to_instance(text, label)
