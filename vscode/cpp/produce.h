#ifndef PRODUCE_H
#define PRODUCE_H
#include "item.h"
class Produce : public Item
{
private:
    std::string color;

public:
    Produce(std::string line) : Item(line)
    {
        color = extractNextAttribute(line);
    }
    Type getType()
    {
        return PRODUCE;
    }
    std::string toString()
    {
        std::stringstream output;
        output.precision(2);
        output << color << " " << Item::toString();
        return output.str();
    }
};

#endif