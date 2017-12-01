/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package y2017.day1

import utils.AdventUtils

fun getSumIfElementInGivenDistanceIsEqual(input: String, distance: Int): Int {
    var sum = 0
    for (i in input.indices) {
        val firstNumber = Character.getNumericValue(input[i])
        val next = (i + distance) % input.length
        val secondNumber = Character.getNumericValue(input[next])
        if (firstNumber == secondNumber) {
            sum += firstNumber
        }
    }

    return sum
}

fun part1(input: String) {
    val sum = getSumIfElementInGivenDistanceIsEqual(input, 1)
    println(sum)
}

fun part2(input: String) {
    val sum = getSumIfElementInGivenDistanceIsEqual(input, input.length/2)
    println(sum)
}

fun main(args: Array<String>) {
    val input = AdventUtils.getInputAsString("inputs/2017/1.txt")
    part1(input)
    part2(input)
}