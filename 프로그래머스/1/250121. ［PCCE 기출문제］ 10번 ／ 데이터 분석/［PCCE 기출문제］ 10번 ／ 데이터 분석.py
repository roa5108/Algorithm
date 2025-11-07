def solution(data, ext, val_ext, sort_by):
    answer = []
    detail = ["code", "date", "maximum", "remain"]
    ext_idx = detail.index(ext)
    sort_idx = detail.index(sort_by)
    for d in data:
        if d[ext_idx]<val_ext:
            answer.append(d)
    answer.sort(key = lambda x : x[sort_idx])
    return answer