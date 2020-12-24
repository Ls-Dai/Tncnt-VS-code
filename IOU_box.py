def iou_box(box_1, box_2):
    # "left bottom" means (left, bottom)
    left_bottom_1 = box_1[0]
    right_top_1 = box_1[1]
    left_bottom_2 = box_2[0]
    right_top_2 = box_2[1]
    # if no "I"
    if left_bottom_1[1] >= right_top_2[1] or left_bottom_1[0] >= right_top_2[0] or left_bottom_2[1] >= right_top_1[1] or right_top_1[0] <= left_bottom_2[0]:
        return 0
    else:
        left = max(left_bottom_1[0], left_bottom_2[0])
        right = min(right_top_1[0], right_top_2[0])
        top = min(right_top_1[1], right_top_2[1])
        bottom = max(left_bottom_1[1], left_bottom_2[1])
        
        width = right - left
        height = top - bottom

        intersection = width * height
        union = (right_top_1[0] - left_bottom_1[0]) * (right_top_1[1] - left_bottom_1[1]) + (right_top_2[0] - left_bottom_2[0]) * (right_top_2[1] - left_bottom_2[1]) - intersection

        # return intersection
        return intersection / union


if __name__ == '__main__':
    box_1 = [(-3, 0), (3, 4)]
    box_2 = [(0, -1), (9, 2)]
    print(iou_box(box_1=box_1, box_2=box_2))

