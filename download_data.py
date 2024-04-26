from huggingface_hub import snapshot_download, hf_hub_download
snapshot_download(repo_id="pscotti/mindeyev2", repo_type = "dataset", revision="main", allow_patterns="*.tar",
    local_dir= "mindeyev2_dataset", local_dir_use_symlinks = False, resume_download = True)
hf_hub_download(repo_id="pscotti/mindeyev2", filename="wds", repo_type="dataset")