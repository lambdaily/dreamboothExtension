from dataclasses import dataclass, field
from typing import Optional

from pydantic import Field

from dreambooth.dataclasses.base_config import BaseConfig


@dataclass
class ControlNetConfig(BaseConfig):
    config_prefix: str = Field("finetune", description="Prefix for the config file.")
    adam_beta1: float = Field(0.9, description="The beta1 parameter for the Adam optimizer.")
    adam_beta2: float = Field(0.999, description="The beta2 parameter for the Adam optimizer.")
    adam_epsilon: float = Field(1e-08, description="Epsilon value for the Adam optimizer.")
    adam_weight_decay: float = Field(1e-2, description="Weight decay to use.")
    attention: str = Field("xformers", description="Whether or not to use xformers.")
    cache_latents: bool = Field(True, description="Cache latents.")
    center_crop: bool = Field(False, description="Whether to center crop the input images to the resolution.")
    checkpoints_total_limit: Optional[int] = Field(None, description="Max number of checkpoints to store.")
    controlnet_model_name_or_path: Optional[str] = field(default=None, metadata={"help": "[CONTROLNET] Path to pretrained controlnet model or model identifier from huggingface.co/models. If not specified controlnet weights are initialized from unet."})
    epoch: Optional[int] = Field(100, description="Lifetime trained epoch.")
    gradient_accumulation_steps: int = field(default=1, metadata={"help": "Number of updates steps to accumulate before performing a backward/update pass."})
    gradient_checkpointing: bool = Field(False, description="Whether or not to use gradient checkpointing.")
    gradient_set_to_none: bool = Field(False, description="Whether or not to set gradients to None when zeroing.")
    graph_smoothing: float = Field(0.1, description="The scale of graph smoothing.")
    input_pertubation: float = Field(0.1, description="[FINE-TUNE] The scale of input pertubation. Recommended 0.1.")
    learning_rate: float = Field(1e-5, description="Initial learning rate.")
    lifetime_revision: Optional[str] = Field(None, description="Current model revision.")
    local_rank: int = Field(-1, description="For distributed training: local_rank")
    lr_num_cycles: int = field(default=1, metadata={"help": "Number of hard resets of the lr in cosine_with_restarts scheduler."})
    lr_power: float = field(default=1.0, metadata={"help": "Power factor of the polynomial scheduler."})
    lr_scheduler: str = Field("linear with warmup", description="The learning rate scheduler to use.")
    lr_warmup_steps: int = Field(500, description="Number of steps for the warmup in the lr scheduler.")
    max_grad_norm: float = Field(1.0, description="Max gradient norm.")
    max_train_samples: Optional[int] = field(default=None, metadata={"help": "For debugging purposes or quicker training, truncate the number of training examples to this value if set."})
    mixed_precision: Optional[str] = Field(None, description="Whether to use mixed precision.",
                                           choices=["no", "fp16", "bf16"])
    model_dir: str = Field("sd-model", description="Base path of the model.")
    model_name: str = Field("sd", description="What to call the model.")
    num_train_epochs: int = Field(100, description="Number of training epochs.")
    num_save_samples: int = Field(4, description="Number of samples to save.")
    offset_noise: float = Field(0, description="[FINE-TUNE] The scale of noise offset.")
    optimizer: str = Field("adamw", description="The optimizer to use.")
    pretrained_model_name_or_path: Optional[str] = field(default=None, metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models."})
    proportion_empty_prompts: float = field(default=0, metadata={"help": "[CONTROLNET] Proportion of image prompts to be replaced with empty strings. Defaults to 0 (no prompt replacement)."})
    random_flip: bool = Field(False, description="[FINE-TUNE] Whether to randomly flip images horizontally.")
    resolution: int = Field(512, description="The resolution for input images.")
    save_ckpt_during: bool = Field(True, description="Save checkpoint during training, instead of weights.")
    save_embedding_every: int = Field(25, description="Save a checkpoint of the training state every X epochs.")
    save_preview_every: int = Field(5, description="Save preview every.")
    snapshot: Optional[str] = Field(None,
                                    description="Whether training should be resumed from a previous checkpoint. Use 'latest' to use the latest checkpoint in the output directory, or specify a revision.")
    scale_lr: bool = Field(False, description="Scale the learning rate.")
    seed: Optional[int] = Field(None, description="A seed for reproducible training.")
    snr_gamma: Optional[float] = Field(5.0, description="[FINE-TUNE] SNR weighting gamma to be used if rebalancing the loss. Recommended value is 5.0.")
    src: str = Field("", description="The source checkpoint.")
    train_batch_size: int = Field(1, description="Batch size for the training dataloader.")
    train_data_dir: Optional[str] = Field(None, description="A folder containing the training data.")
    use_ema: bool = Field(False, description="[FINE-TUNE] Whether to use EMA model.")
    use_dir_tags: bool = Field(False, description="[FINE-TUNE] Whether to use the directory name as the tag. Will be appended if not found in the caption.")
    v2: bool = Field(False, description="If this is a V2 Model or not.")
