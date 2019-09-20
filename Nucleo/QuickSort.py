class QuickSort:
	def partition(self,arr,low,high):
		i = (low-1)
		pivot = arr[high]

		for j in range(low,high):

			if arr[j] <= pivot:

				i = i+1
				arr[i],arr[j] = arr[j],arr[i]

		arr[i+1],arr[high] = arr[high],arr[i+1]
		return (i+1)

	def quickSort(self,arr,low,high):
		if low < high:
			pi = self.partition(arr,low,high)

			self.quickSort(arr,low,pi-1)
			self.quickSort(arr,pi+1,high)

	def sort (self,data=[]):
		return self.quickSort(data,0,len(data)-1)