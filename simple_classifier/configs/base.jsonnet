local embedding_dim = 50;

// For more info on config files generally, see https://guide.allennlp.org/using-config-files
{
    "dataset_reader" : {
        // This name needs to match the name that you used to register your dataset reader, with
        // the call to `@DatasetReader.register()`.
        "type": "yelp-review-jsonl",
        // These other parameters exactly match the constructor parameters of your dataset reader class.
        "token_indexers": {
            "tokens": {
                "type": "single_id"
            }
        }
    },
    "train_data_path": "data/train_5000.jsonl",
    "validation_data_path": "data/dev_500.jsonl",
    "model": {
        // This name needs to match the name that you used to register your model, with
        // the call to `@Model.register()`.
        "type": "simple_classifier",
        // These other parameters exactly match the constructor parameters of your model class.
        "embedder": {
            "token_embedders": {
                "tokens": {
                    "type": "embedding",
                    "embedding_dim": embedding_dim
                }
            }
        },
        "encoder": {
            "type": "bag_of_embeddings",
            "embedding_dim": embedding_dim
        }
    },
    "data_loader": {
        // See http://docs.allennlp.org/master/api/data/dataloader/ for more info on acceptable
        // parameters here.
        "batch_size": 8,
        "shuffle": true
    },
    "trainer": {
        // See http://docs.allennlp.org/master/api/training/trainer/#gradientdescenttrainer-objects
        // for more info on acceptable parameters here.
        "optimizer": "huggingface_adamw",
        "num_epochs": 5,
        // Force use of the CPU. If not passed, AllenNLP will automatically use a GPU if one is available.
        "cuda_device": -1
    }
    // There are a few other optional parameters that can go at the top level, e.g., to configure
    // vocabulary behavior, to use a separate dataset reader for validation data, or other things.
    // See http://docs.allennlp.org/master/api/commands/train/#from_partial_objects for more info
    // on acceptable parameters.
}
