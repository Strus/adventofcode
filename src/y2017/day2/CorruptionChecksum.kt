/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package y2017.day2

import sun.font.TrueTypeFont
import utils.AdventUtils

fun part1(input: List<String>) {
    var checksum = 0
    for (line in input) {
        val values = line.split("\t").map { it.toInt() }
        checksum += values.max()!! - values.min()!!
    }

    println(checksum)
}

fun part2(input: List<String>) {
    // this solution is ugly, I don't like it, but I don't have
    // time right now to think more about it
    var checksum = 0
    var found = false
    for (line in input) {
        val values = line.split("\t").map { it.toInt() }
        for (value1 in values) {
            for (value2 in values) {
                if (value1 % value2 == 0 && value1 != value2) {
                    checksum += value1 / value2
                    found = true
                    break
                }
            }

            if (found) {
                found = false
                break
            }
        }
    }

    println(checksum)
}

fun main(args: Array<String>) {
    val input = AdventUtils.getInputAsList("inputs/2017/2.txt")
    part1(input)
    part2(input)
}

