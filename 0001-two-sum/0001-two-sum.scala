object Solution {
    def twoSum(numbers: Array[Int], target: Int): Array[Int] = {
        val map = scala.collection.mutable.Map[Int, Int] ()
        var count = 0;
        
        for(number <- numbers){
            val compare = target - number
            map.get(compare) match {
                case None => {map.put(number,count)}
                case Some(index) => return Array(index,count) 
            }
            count = count+1
        }
        Array(0,0)
    }
}
