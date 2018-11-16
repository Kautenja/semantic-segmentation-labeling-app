"""Test cases for the brush_cursor module."""
from unittest import TestCase
import numpy as np
from ..cursor import make_circle
from ..cursor import make_cursor
from ..cursor import pyglet_cursor


class ShouldCreateCircleWithRadius1(TestCase):
    def test(self):
        circle = make_circle(1)
        expected = np.array([
            [0, 0, 0,],
            [0, 1, 0,],
            [0, 0, 0,],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCircleWithRadius2(TestCase):
    def test(self):
        circle = make_circle(2)
        expected = np.array([
            [0, 0, 0, 0, 0,],
            [0, 1, 1, 1, 0,],
            [0, 1, 1, 1, 0,],
            [0, 1, 1, 1, 0,],
            [0, 0, 0, 0, 0,],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCircleWithRadius3(TestCase):
    def test(self):
        circle = make_circle(3)
        expected = np.array([
            [0, 0, 0, 0, 0, 0, 0,],
            [0, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 0,],
            [0, 0, 0, 0, 0, 0, 0,],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCircleWithRadius10(TestCase):
    def test(self):
        circle = make_circle(10)
        expected = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCursorWithRadius1(TestCase):
    def test(self):
        circle = make_cursor(1, color=(33, 66, 99))
        expected = np.array([
            [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCursorWithRadius2(TestCase):
    def test(self):
        circle = make_cursor(2, color=(33, 66, 99))
        expected = np.array([
            [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldCreateCursorWithRadius3(TestCase):
    def test(self):
        circle = make_cursor(3, color=(33, 66, 99))
        expected = np.array([
            [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [ 33,  66,  99, 255,],
                [  0,   0,   0,   0,],
            ], [
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
                [  0,   0,   0,   0,],
            ],
        ])
        self.assertTrue(np.array_equal(expected, circle))


class ShouldMakePygletCursor(TestCase):
    def test(self):
        cursor = make_cursor(3, color=(33, 66, 99))
        mouse_cursor = pyglet_cursor(cursor)