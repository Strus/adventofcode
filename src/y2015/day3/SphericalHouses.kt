/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package y2015.day3

import utils.AdventUtils

class MovingSanta {
    data class Position(var x: Int, var y: Int)

    var position = Position(0, 0)
    var visitedPositions: MutableList<Position> = mutableListOf(Position(0, 0))
    var housesVisited: Int = 1

    fun moveRight() {
        position.x++
        evaluatePosition()
    }
    fun moveLeft() {
        position.x--
        evaluatePosition()
    }
    fun moveUp() {
        position.y++
        evaluatePosition()
    }
    fun moveDown() {
        position.y--
        evaluatePosition()
    }

    fun removeHousesOtherSantaVisited(otherSanta: MovingSanta) {
        for (position in visitedPositions) {
            if (otherSanta.visitedPositions.find { it == position } != null) {
                housesVisited--
            }
        }
    }

    private fun evaluatePosition() {
        if (visitedPositions.find{ it == position } == null) {
            visitedPositions.add(Position(position.x, position.y))
            housesVisited++
        }
    }
}

fun part1(input: String) {
    val santa = MovingSanta()
    for (direction in input) {
        when (direction) {
            '>' -> santa.moveRight()
            '<' -> santa.moveLeft()
            '^' -> santa.moveUp()
            'v' -> santa.moveDown()
        }
    }
    println(santa.housesVisited)
}

fun part2(input: String) {
    val santa = MovingSanta()
    val roboSanta = MovingSanta()
    var currentSanta = santa
    for (direction in input) {
        when (direction) {
            '>' -> currentSanta.moveRight()
            '<' -> currentSanta.moveLeft()
            '^' -> currentSanta.moveUp()
            'v' -> currentSanta.moveDown()
        }

        currentSanta = if (currentSanta == santa) roboSanta else santa
    }
    roboSanta.removeHousesOtherSantaVisited(santa)
    println(santa.housesVisited + roboSanta.housesVisited)
}

fun main(args: Array<String>) {
    val input = AdventUtils.getInputAsString("inputs/2015/3.txt")
    part1(input)
    part2(input)
}