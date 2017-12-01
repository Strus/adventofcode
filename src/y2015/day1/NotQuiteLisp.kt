/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package y2015.day1

import utils.AdventUtils

fun moveToNextFloor(currentFloor: Int, direction: Char): Int {
    when (direction) {
        '(' -> return currentFloor + 1
        ')' -> return currentFloor - 1
    }

    throw IllegalArgumentException("Direction must be either ( or ) character!")
}

fun part1(input: String) {
    var floor = 0
    input.forEach{ floor = moveToNextFloor(floor, it) }

    println(floor)
}

fun part2(input: String) {
    var floor = 0
    for (i in input.indices) {
        floor = moveToNextFloor(floor, input[i])

        if (floor == -1) {
            println(i + 1)
            break
        }
    }
}

fun main(args: Array<String>) {
    val input = AdventUtils.getInputAsString("inputs/2015/1.txt")
    part1(input)
    part2(input)
}
