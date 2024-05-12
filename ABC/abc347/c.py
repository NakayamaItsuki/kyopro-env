


N, A, B = map(int, input().split())

Ds = list(map(int, input().split()))

num_day_per_week = A + B

Ds_max = max(Ds) % num_day_per_week
Ds_min = min(Ds) % num_day_per_week

# if Ds_max < Ds_min:
#     Ds_band = Ds_max + num_day_per_week - Ds_min + 1

# else:
#     Ds_band = Ds_max - Ds_min + 1


Ds_band = Ds_max - Ds_min + 1

if Ds[0] % num_day_per_week > Ds[-1] % num_day_per_week:
    Ds_band = num_day_per_week - Ds_band

if Ds_band <= A:
    print('Yes')
    
else:
    print('No')
    
print(Ds_band)
    
    

# N, A, B = map(int, input().split())

# Ds = list(map(int, input().split()))

# num_day_per_week = A + B

# # 各日付を週の何日目かに変換
# week_days = set([D % num_day_per_week for D in Ds])

# # print(week_days)

# # 週の中での最小日と最大日を見つける
# min_day = min(week_days)
# max_day = max(week_days)

# # すべての日付が同じ週にあり、かつ休日範囲内にあるかを判断
# if max_day - min_day < num_day_per_week and max_day - min_day < A:
#     print('Yes')
# else:
#     print('No')


# N, A, B = map(int, input().split())

# Ds = list(map(int, input().split()))

# num_day_per_week = A + B

# Ds_set = set([D % num_day_per_week for D in Ds])

# Ds_band = max(Ds_set) - min(Ds_set) + 1

# # if len(Ds_set) == 1:
# #     Ds_band = 1

# # else:
# #     Ds_band = max(Ds_set) - min(Ds_set) + 1

# if Ds_band <= A:
#     print('Yes')
    
# else:
#     print('No')
    
# print(Ds_band)


# N, A, B = map(int, input().split())

# Ds = list(map(int, input().split()))

# num_day_per_week = A + B

# # Ds_set = set()
# # for D in Ds:
# #     if D % num_day_per_week == 0:
# #         Ds_set.add(num_day_per_week)
# #     else:
# #         Ds_set.add(D % num_day_per_week)

# # # Ds_band = max(Ds_set) - min(Ds_set) + 1

# # Ds_band = 0

# Ds_max = max(Ds) % num_day_per_week
# Ds_min = min(Ds) % num_day_per_week

# if Ds_max < Ds_min:
#     Ds_band = Ds_max + num_day_per_week - Ds_min + 1

# else:
#     Ds_band = Ds_max - Ds_min + 1


# if Ds_band <= A:
#     print('Yes')
    
# else:
#     print('No')
    
# print(Ds_band)



# N, A, B = map(int, input().split())

# Ds = list(map(int, input().split()))


# # is_holiday = [None] + [True] * A + [False] * B
    
# num_day_per_week = A + B

# Ds_set = set()
# for D in Ds:
#     if D % num_day_per_week == 0:
#         Ds_set.add(num_day_per_week)
#     else:
#         Ds_set.add(D % num_day_per_week)

# # print(Ds_set)


# Ds_band = max(Ds_set) - min(Ds_set) + 1

# # print(Ds_band)

# if Ds_band <= A:
#     print('Yes')
    
# else:
#     print('No')






# Ds_min = min(Ds_set)
# Ds_max = max(Ds_set)

# # 1週間の各日で．
# # for day in range(num_day_per_week - Ds_max + 1):
# for day in range(num_day_per_week - Ds_max + 1):
    
#     flag = True
    
#     for D in Ds:
        
#         # 休日ではなかったらスキップ
#         if not is_holiday[(day + D) % num_day_per_week]:
            
#             flag = False
#             break
    
#     if flag:
#         print('Yes')
#         exit()
        
# print('No')


# # # 1週間の各日でforを回すとTLE

# # # 予定がある日を作成する

# # N, A, B = map(int, input().split())

# # Ds = list(map(int, input().split()))

# # num_day_per_week = A + B

# # holiday_set = set(range(1,A+1))

# # scheduled_days_set = set([(D+1) % num_day_per_week for D in Ds])




# # # # 休日の集合に予定がある日が含まれていたらYes
# # # if holiday_set >= scheduled_days_set:
# # #     print('Yes')
# # # else:
# # #     print('No')
    

# # print(holiday_set, scheduled_days_set)



# def can_all_schedules_be_holidays(N, A, B, D):
#     # 1週間の長さ
#     week_length = A + B

#     # 各予定日が休日かどうかのチェック
#     for day in D:
#         # 1週間のサイクルにおける位置を計算
#         day_in_cycle = day % week_length
        
#         # 位置が0の場合は末尾の日に対応するので調整
#         if day_in_cycle == 0:
#             day_in_cycle = week_length

#         # その日が平日であれば、全ての予定が休日になる可能性はない
#         if day_in_cycle > A:
#             return "No"
    
#     return "Yes"

# # 結果をチェック
# print(can_all_schedules_be_holidays(N, A, B, Ds))


# # 1週間の長さ
# week_length = A + B

# # 各予定日が休日かどうかのチェック
# for day in Ds:
#     # 1週間のサイクルにおける位置を計算
#     day_in_cycle = day % week_length
    
#     # 位置が0の場合は末尾の日に対応するので調整
#     if day_in_cycle == 0:
#         day_in_cycle = week_length

#     # その日が平日であれば、全ての予定が休日になる可能性はない
#     if day_in_cycle > A:
#         print("No")
#         exit()

# # print("Yes")


# import numpy as np

# Ds = np.array(Ds)

# # 各予定が休日であるかどうかを計算
# # 1週間の周期で休日かどうかを判断し、休日なら True、そうでなければ False
# is_holiday = np.logical_and(1 <= Ds % (A + B), Ds % (A + B) <= A)
# # 休日の最終日の場合は、D % (A + B) == 0 となるので、その場合も考慮
# is_holiday = np.logical_or(is_holiday, Ds % (A + B) == 0)

# # すべての予定が休日であるかどうか
# all_holidays = np.all(is_holiday)

# # 結果の出力
# result = "Yes" if all_holidays else "No"
# print(result)




