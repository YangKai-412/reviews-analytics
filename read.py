
def read_file(filename):
	data = []
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
			count += 1 #count = count + 1
			if count % 1000 == 0:   #％是用來求餘數
				print(len(data))	#當你是一千的倍數就印出來
	print('檔案讀取完了,總共有', len(data), '筆資料')

	sum_len = 0
	for d in data:
		sum_len += len(d)	
	print('留言的平均長度為', sum_len/len(data))

	new = []
	for d in data:
		if len(d) < 100:
			new.append(d)
	print('一共有', len(new), '筆留言長度小於100')
	print(new[0])


	good = []
	for d in data:
		if 'good' in d:
			good.append(d)

	#good = [d for d in data if 'good' in d] #上面四行快寫法

	print('一共有', len(good), '筆留言提到good')
	print(good[0])
	return data

	#bad = ['bad' in d for d in data]
	#print(bad)	#此行印出 一百萬筆 True or False 運算


# 文字計數
def count(data):
	wc = {} # word_count
	for d in data:
		words = d.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1 #新增新的 key 進 wc 字典
	for word in wc:
		if wc[word] > 1000000:
			print(word, wc[word])

	print(len(wc))

	while True:
		word = input('請問你想查什麼字： ')
		if word == 'q':
			break
		if word in wc:
			print(word, '出現過的次數為： ', wc[word])
		else:
			print('查無此字')

	print('謝謝使用查詢')


def main():
	data = read_file('reviews.txt')
	count(data)
	

main()