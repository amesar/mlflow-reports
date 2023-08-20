
MLflow Model: _models:/dbdemos_pcb_classification/1_
====================================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
* [Registered Model](#registered-model)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)
* [Registered Model Version](#registered-model-version)
	* [Details](#details)
	* [Tags](#tags)
* [Run](#run)
	* [Info](#info)
	* [Params](#params)
	* [Metrics](#metrics)
	* [Inputs](#inputs)
	* [Tags](#tags)
* [Experiment](#experiment)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)

# Model Overview
  
<b><font size="+1">MLflow Model</font></b>  

|Name|Value|
| :--- | :--- |
|model_uri|models:/dbdemos_pcb_classification/1|
|flavor|None|
|flavor_version||
|mlflow_version|2.3.1|
|size_bytes|343,271,516|
|databricks_runtime|13.1.x-gpu-ml-scala2.12|
|is_unity_catalog|False|
|time_created|2023-08-02 08:18:11|
|report_time|2023-08-20 17:24:32|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/dbdemos_pcb_classification/1|
|run_uri|runs:/815123f2db9b49cdb9790c6a0371a4da/model|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/4e3ac9ee6e464efd88270d84dfd54c12/models/model|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814239786/815123f2db9b49cdb9790c6a0371a4da/artifacts/model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|model|
|databricks_runtime|13.1.x-gpu-ml-scala2.12|
|mlflow_version|2.3.1|
|model_uuid|3c21c7a008da4727b96a99b44fb72151|
|run_id|815123f2db9b49cdb9790c6a0371a4da|
|utc_time_created|2023-08-02 08:18:11.144619|
|model_flavor|transformers|
|model_size_bytes|343271516|

### Flavors

#### Flavor 'transformers'
  

|Name|Value|
| :--- | :--- |
|code|None|
|components|['tokenizer', 'image_processor']|
|image_processor_type|ViTFeatureExtractor|
|instance_type|ImageClassificationPipeline|
|pipeline|pipeline|
|pipeline_model_type|ViTForImageClassification|
|source_model_name|/tmp/huggingface/pcb/vit-base-patch16-224-finetuned-leaf/checkpoint-2410|
|task|image-classification|
|tokenizer_type|ViTFeatureExtractor|
|transformers_version|4.28.1|

## Signature
  
**_<font color="red" size="+1">None found</font>_**
## Saved input example info
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|dbdemos_pcb_classification|
|creation_timestamp|1690964304680|
|last_updated_timestamp|1691232517478|
|user_id|andre@mycompany.com|
|id|b4e61c7c063440149cd2439490075737|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-08-02 08:18:25|
|_last_updated_timestamp|2023-08-05 10:48:37|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/dbdemos_pcb_classification|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=dbdemos_pcb_classification|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the details of the registered model and its model versions, and use the model versions."
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view and edit the details of a registered model and its model versions (except stage changes), and add new model versions."
    },
    {
      "permission_level": "CAN_MANAGE_STAGING_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between non-Production stages."
    },
    {
      "permission_level": "CAN_MANAGE_PRODUCTION_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between any stages."
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can manage permissions on, view all details of, and perform all actions on the registered model and its model versions."
    }
  ],
  "permissions": {
    "object_id": "/registered-models/b4e61c7c063440149cd2439490075737",
    "object_type": "registered-model",
    "access_control_list": [
      {
        "group_name": "admins",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "group_name": "users",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "user_name": "andre@mycompany.com",
        "display_name": "Andre",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": false
          }
        ]
      },
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "service-principal-e2-demo-west-ws-do-not-delete",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      }
    ]
  }
}

```
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|dbdemos_pcb_classification|
|version|1|
|creation_timestamp|1690964304928|
|last_updated_timestamp|1691232517478|
|user_id|andre@mycompany.com|
|current_stage|Staging|
|source|dbfs:/databricks/mlflow-tracking/3428923814239786/815123f2db9b49cdb9790c6a0371a4da/artifacts/model|
|run_id|815123f2db9b49cdb9790c6a0371a4da|
|status|READY|
|_creation_timestamp|2023-08-02 08:18:25|
|_last_updated_timestamp|2023-08-05 10:48:37|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/4e3ac9ee6e464efd88270d84dfd54c12/models/model|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814239786/815123f2db9b49cdb9790c6a0371a4da/artifacts/model|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/dbdemos_pcb_classification/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=dbdemos_pcb_classification&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|815123f2db9b49cdb9790c6a0371a4da|
|run_uuid|815123f2db9b49cdb9790c6a0371a4da|
|experiment_id|3428923814239786|
|run_name|hugging_face|
|status|FINISHED|
|start_time|1690961357276|
|end_time|1690964297725|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3428923814239786/815123f2db9b49cdb9790c6a0371a4da/artifacts|
|lifecycle_stage|active|
|_start_time|2023-08-02 07:29:17|
|_end_time|2023-08-02 08:18:18|
|_duration|2940.449|
|_experiment_name|/Users/andre@mycompany.com/experiments/dbdemos/computer-vision-dl/pcb|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3428923814239786/runs/815123f2db9b49cdb9790c6a0371a4da|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=815123f2db9b49cdb9790c6a0371a4da|

## Params
  

|Param|Value|
| :--- | :--- |
|_name_or_path|google/vit-base-patch16-224|
|adafactor|False|
|adam_beta1|0.9|
|adam_beta2|0.999|
|adam_epsilon|1e-08|
|add_cross_attention|False|
|architectures|['ViTForImageClassification']|
|attention_probs_dropout_prob|0.0|
|auto_find_batch_size|False|
|bad_words_ids|None|
|begin_suppress_tokens|None|
|bf16|False|
|bf16_full_eval|False|
|bos_token_id|None|
|chunk_size_feed_forward|0|
|cross_attention_hidden_size|None|
|data_seed|None|
|dataloader_drop_last|False|
|dataloader_num_workers|0|
|dataloader_pin_memory|True|
|ddp_bucket_cap_mb|None|
|ddp_find_unused_parameters|None|
|ddp_timeout|1800|
|debug|[]|
|decoder_start_token_id|None|
|deepspeed|None|
|disable_tqdm|False|
|diversity_penalty|0.0|
|do_eval|True|
|do_predict|False|
|do_sample|False|
|do_train|False|
|early_stopping|False|
|encoder_no_repeat_ngram_size|0|
|encoder_stride|16|
|eos_token_id|None|
|eval_accumulation_steps|None|
|eval_delay|0|
|eval_steps|None|
|evaluation_strategy|epoch|
|exponential_decay_length_penalty|None|
|finetuning_task|None|
|forced_bos_token_id|None|
|forced_eos_token_id|None|
|fp16|False|
|fp16_backend|auto|
|fp16_full_eval|False|
|fp16_opt_level|O1|
|fsdp|[]|
|fsdp_config|{'fsdp_min_num_params': 0, 'xla': False, 'xla_fsdp_grad_ckpt': False}|
|fsdp_min_num_params|0|
|fsdp_transformer_layer_cls_to_wrap|None|
|full_determinism|False|
|gradient_accumulation_steps|1|
|gradient_checkpointing|False|
|greater_is_better|True|
|group_by_length|False|
|half_precision_backend|auto|
|hidden_act|gelu|
|hidden_dropout_prob|0.0|
|hidden_size|768|
|hub_model_id|None|
|hub_private_repo|False|
|hub_strategy|every_save|
|hub_token|<HUB_TOKEN>|
|id2label|{0: 'normal', 1: 'damaged'}|
|ignore_data_skip|False|
|image_size|224|
|include_inputs_for_metrics|False|
|initializer_range|0.02|
|intermediate_size|3072|
|is_decoder|False|
|is_encoder_decoder|False|
|jit_mode_eval|False|
|label2id|{'normal': 0, 'damaged': 1}|
|label_names|None|
|label_smoothing_factor|0.0|
|layer_norm_eps|1e-12|
|learning_rate|5e-05|
|length_column_name|length|
|length_penalty|1.0|
|load_best_model_at_end|True|
|local_rank|0|
|log_level|passive|
|log_level_replica|warning|
|log_on_each_node|True|
|logging_dir|/tmp/huggingface/pcb/vit-base-patch16-224-finetuned-leaf/runs/Aug02_07-29-08_0802-063411-pb0ujrfr-10-0-3-133|
|logging_first_step|False|
|logging_nan_inf_filter|True|
|logging_steps|10|
|logging_strategy|steps|
|lr_scheduler_type|linear|
|max_grad_norm|1.0|
|max_length|20|
|max_steps|-1|
|metric_for_best_model|f1|
|min_length|0|
|model_type|vit|
|mp_parameters||
|no_cuda|False|
|no_repeat_ngram_size|0|
|num_attention_heads|12|
|num_beam_groups|1|
|num_beams|1|
|num_channels|3|
|num_hidden_layers|12|
|num_return_sequences|1|
|num_train_epochs|20|
|optim|adamw_hf|
|optim_args|None|
|output_attentions|False|
|output_dir|/tmp/huggingface/pcb/vit-base-patch16-224-finetuned-leaf|
|output_hidden_states|False|
|output_scores|False|
|overwrite_output_dir|False|
|pad_token_id|None|
|past_index|-1|
|patch_size|16|
|per_device_eval_batch_size|32|
|per_device_train_batch_size|32|
|per_gpu_eval_batch_size|None|
|per_gpu_train_batch_size|None|
|prediction_loss_only|False|
|prefix|None|
|problem_type|None|
|pruned_heads|{}|
|push_to_hub|False|
|push_to_hub_model_id|None|
|push_to_hub_organization|None|
|push_to_hub_token|<PUSH_TO_HUB_TOKEN>|
|qkv_bias|True|
|ray_scope|last|
|remove_invalid_values|False|
|remove_unused_columns|False|
|repetition_penalty|1.0|
|report_to|['mlflow', 'tensorboard']|
|resume_from_checkpoint|None|
|return_dict|True|
|return_dict_in_generate|False|
|run_name|/tmp/huggingface/pcb/vit-base-patch16-224-finetuned-leaf|
|save_on_each_node|False|
|save_safetensors|False|
|save_steps|500|
|save_strategy|epoch|
|save_total_limit|None|
|seed|42|
|sep_token_id|None|
|sharded_ddp|[]|
|skip_memory_metrics|True|
|suppress_tokens|None|
|task_specific_params|None|
|temperature|1.0|
|tf32|None|
|tf_legacy_loss|False|
|tie_encoder_decoder|False|
|tie_word_embeddings|True|
|tokenizer_class|None|
|top_k|50|
|top_p|1.0|
|torch_compile|False|
|torch_compile_backend|None|
|torch_compile_mode|None|
|torch_dtype|None|
|torchdynamo|None|
|torchscript|False|
|tpu_metrics_debug|False|
|tpu_num_cores|None|
|transformers_version|4.28.1|
|typical_p|1.0|
|use_bfloat16|False|
|use_ipex|False|
|use_legacy_prediction_loop|False|
|use_mps_device|False|
|warmup_ratio|0.1|
|warmup_steps|0|
|weight_decay|0.0|
|xpu_backend|None|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|epoch|15.0|
|eval_f1|0.9945694336695112|
|eval_loss|0.006073087453842163|
|eval_runtime|17.9988|
|eval_samples_per_second|214.07|
|eval_steps_per_second|6.723|
|learning_rate|1.388888888888889e-05|
|loss|0.0001|
|total_flos|1.7913435348529054e+19|
|train_loss|0.040428217096158583|
|train_runtime|2930.6453|
|train_samples_per_second|105.171|
|train_steps_per_second|3.289|

## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|3306527556979248248_7842249936114663509_dacf43fdc36a4ede9d1f28803a51c0f5|
|mlflow.databricks.notebookID|3428923814239730|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/dbdemos/computer-vision-pcb/02-huggingface-model-training-Andre|
|mlflow.databricks.notebookRevisionID|1690964298173|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0802-063411-pb0ujrfr|
|mlflow.databricks.cluster.info|{'cluster_name': 'dbdemos-computer-vision-pcb-andre', 'spark_version': '13.1.x-gpu-ml-scala2.12', 'node_type_id': 'g5.2xlarge', 'driver_node_type_id': 'g5.2xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'num_workers': 0}|
|mlflow.databricks.cluster.libraries|{'installable': [], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|
|mlflow.databricks.workspaceID|2556758628403379|
|mlflow.databricks.workspaceURL|e2-demo-west.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Users/andre@mycompany.com/dbdemos/computer-vision-pcb/02-huggingface-model-training-Andre|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'model', 'flavors': {'transformers': {'task': 'image-classification', 'source_model_name': '/tmp/huggingface/pcb/vit-base-patch16-224-finetuned-leaf/checkpoint-2410', 'components': ['tokenizer', 'image_processor'], 'pipeline': 'pipeline', 'code': None, 'image_processor_type': 'ViTFeatureExtractor', 'tokenizer_type': 'ViTFeatureExtractor', 'pipeline_model_type': 'ViTForImageClassification', 'instance_type': 'ImageClassificationPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '815123f2db9b49cdb9790c6a0371a4da', 'model_uuid': '3c21c7a008da4727b96a99b44fb72151', 'utc_time_created': '2023-08-02 08:18:11.144619', 'mlflow_version': '2.3.1', 'databricks_runtime': '13.1.x-gpu-ml-scala2.12'}]|
|mlflow.runName|hugging_face|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|dbdemos|pcb_classification|
|sparkDatasourceInfo|[{'path': 's3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/tables/9020abb0-5741-4f42-9b3c-7bc72dad583a', 'version': '43', 'format': 'delta'}]|

### Exploded Tags

#### Spark Datasources
  

|Format|Version|Path|
| :--- | :--- | :--- |
|delta|43|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/tables/9020abb0-5741-4f42-9b3c-7bc72dad583a|

#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0802-063411-pb0ujrfr|
|cluster_name|dbdemos-computer-vision-pcb-andre|
|spark_version|13.1.x-gpu-ml-scala2.12|
|node_type_id|g5.2xlarge|
|driver_node_type_id|g5.2xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_count': 0}|
|num_workers|0|

#### Cluster Libraries

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|3428923814239786|
|name|/Users/andre@mycompany.com/experiments/dbdemos/computer-vision-dl/pcb|
|artifact_location|dbfs:/databricks/mlflow-tracking/3428923814239786|
|lifecycle_stage|active|
|last_update_time|1690961357276|
|creation_time|1690961026005|
|_creation_time|2023-08-02 07:23:46|
|_last_update_time|2023-08-02 07:29:17|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3428923814239786|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3428923814239786|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/experiments/dbdemos/computer-vision-dl/pcb|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experimentType|MLFLOW_EXPERIMENT|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the experiment"
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view, log runs, and edit the experiment"
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can view, log runs, edit, delete, and change permissions of the experiment"
    }
  ],
  "permissions": {
    "object_id": "/experiments/3428923814239786",
    "object_type": "mlflowExperiment",
    "access_control_list": [
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "service-principal-e2-demo-west-ws-do-not-delete",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/directories/"
            ]
          }
        ]
      },
      {
        "user_name": "andre@mycompany.com",
        "display_name": "Andre",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/directories/767933989557963"
            ]
          }
        ]
      },
      {
        "group_name": "admins",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/directories/"
            ]
          }
        ]
      }
    ]
  }
}

```