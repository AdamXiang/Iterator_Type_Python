from polygon import Polygon
from polygons import Polygons

def main():
    # Create a Polygons sequence with max vertices = 10 and circumradius = 5
    polygons = Polygons(10, 5)
    print(polygons)  
    # Output: Polygons(m=10, R=5)

    # Length of the sequence (polygons from 3-gon up to 10-gon)
    print(f"Number of polygons: {len(polygons)}")  
    # Output: 8 (3-gon to 10-gon inclusive)

    # Indexing and slicing
    print("First polygon:", polygons[0])   # Polygon with 3 vertices (triangle)
    print("Last polygon:", polygons[-1])   # Polygon with 10 vertices

    print("Slice [2:5]:", polygons[2:5])   # Returns polygons with 5–7 vertices

    # Access properties of a specific polygon
    hexagon = polygons[3]  # Polygon with 6 vertices
    print(f"Hexagon - sides: {hexagon.count_edges}, area: {hexagon.area:.2f}, perimeter: {hexagon.perimeter:.2f}")

    # Find the most efficient polygon (max area-to-perimeter ratio)
    best = polygons.max_efficiency_polygon
    print(f"Most efficient polygon: {best.count_vertices}-gon with efficiency {best.area/best.perimeter:.4f}")

if __name__ == "__main__":
    main()
