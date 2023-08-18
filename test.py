import torch


a = torch.ones((1, 2, 3))
a = a.cuda()  # 将会执行 a.mlu()


print(a.device)  # 输出结果: mlu


b = torch.ones((4, 5, 6))
b = b.to("cuda")  # 将会执行 a.mlu()

print(b.device)  # 输出结果: mlu


torch.full((7,8,9), 0.5, device= "cuda")