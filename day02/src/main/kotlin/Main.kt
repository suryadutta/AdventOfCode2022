import java.io.File

internal fun getInput(filename: String) = File("src/data/$filename.txt").inputStream().readBytes().toString(Charsets.UTF_8)

fun part1() {
    val input = getInput("day2").lines()
}

fun part2() {
    val input = getInput("day2").lines()
}

fun main(args: Array<String>) {
    part1()
    part2()
}