/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package y2015.day2

import utils.AdventUtils

fun getDimensionsAsInts(line: String): List<Int> {
    val dimensionsStrings = line.split("x")
    val dimensions = mutableListOf<Int>()
    dimensionsStrings.mapTo(dimensions) { it.toInt() }

    return dimensions
}

fun part1(input: List<String>) {
    var totalSquareFeet = 0
    for (line in input) {
        val dimensions = getDimensionsAsInts(line)

        val sides = listOf(2 * dimensions[0] * dimensions[1],
                           2 * dimensions[1] * dimensions[2],
                           2 * dimensions[0] * dimensions[2])
        val bonus = sides.min()!!
        totalSquareFeet += bonus/2 + sides.sum()
    }
    println(totalSquareFeet)
}

fun part2(input: List<String>) {
    var totalFeet = 0
    for (line in input) {
        val dimensions: MutableList<Int> = getDimensionsAsInts(line) as MutableList<Int>

        val bowLength = dimensions[0] * dimensions[1] * dimensions[2]

        val firstShortestDimension = dimensions.min()!!
        dimensions.remove(firstShortestDimension)

        val secondShortestDimension = dimensions.min()!!
        totalFeet += bowLength + 2 * firstShortestDimension + 2 * secondShortestDimension
    }
    println(totalFeet)
}

fun main(args: Array<String>) {
    val input = AdventUtils.getInputAsList("inputs/2015/2.txt")
    part1(input)
    part2(input)
}