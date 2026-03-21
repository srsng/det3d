def main():
    print("Hello from det3d!")
    import mmdet3d
    import mmcv
    import torch
    import mmdet
    
    print(f"{mmdet3d.__version__=}")
    print(f"{mmdet.__version__=}")
    print(f"{mmcv.__version__=}")
    print(f"{torch.version.__version__=}")
    
    assert mmdet3d.__version__=='1.4.0'
    assert mmdet.__version__=='3.3.0'
    assert mmcv.__version__=='2.1.0'
    assert torch.version.__version__=='2.1.2+cu121'
    
if __name__ == "__main__":
    main()
