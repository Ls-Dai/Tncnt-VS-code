# Tncnt-VS-code

## IOU for boxes
情况：
1. 有没有重叠
2. 有重叠，计算

demo:

![demo1_input](demo_1_input.jpg)

![demo1_output](demo_1_output.jpg)

## IOU for masks
交：

1. np.array 的相乘

并：

2. np.array 的相加，然后clip，放缩到 `[0,1]`

demo:

![demo2_input](demo_2_input.jpg)

![demo2_output](demo_2_output.jpg)

